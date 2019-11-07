provider "aws"{
region ="ap-south-1"
}

locals {
  az_names        = "${data.aws_availability_zones.azs.names}"
  pub_sub_ids     = "${aws_subnet.public.*.id}"
  private_sub_ids = "${aws_subnet.private.*.id}"
}

resource "aws_vpc" "my_vpc" {
  cidr_block       = "${var.vpc_cidr}"
  instance_tenancy = "${var.vpc_tenancy}"

  tags = "${var.vpc_tags}"
}

resource "aws_subnet" "public" {

  count                   = "${length(local.az_names)}"
  vpc_id                  = "${aws_vpc.my_vpc.id}"
  cidr_block              = "${cidrsubnet(var.vpc_cidr, 8, count.index)}"
  map_public_ip_on_launch = true
  availability_zone       = "${local.az_names[count.index]}"
  tags = {
    Name = "Subnet-${count.index + 1}-${terraform.workspace}"
  }
}


# Create Internet Gatewway for Public subnets

resource "aws_internet_gateway" "igw" {
  vpc_id = "${aws_vpc.my_vpc.id}"

  tags = {
    Name        = "IGW"
    Environment = "${terraform.workspace}"
  }
}

resource "aws_route_table" "pub_rt" {
  vpc_id = "${aws_vpc.my_vpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.igw.id}"
  }

  tags = {
    Name        = "PubRT"
  }
}


# Public subnet and route table association

resource "aws_route_table_association" "pub_rt_association" {
  count          = "${length(local.az_names)}"
  subnet_id      = "${local.pub_sub_ids[count.index]}"
  route_table_id = "${aws_route_table.pub_rt.id}"
}
output "az_names" {
  value = "${local.az_names}"
}

data "aws_availability_zones" "azs" {

}
resource "aws_instance" "web" {
  count = "${var.web_instance_count}"
  # ami           = "${data.aws_ami.web.id}"
  ami                    = "${var.web_amis[var.region]}"
  instance_type          = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.web.id}"]
  subnet_id              = "${local.pub_sub_ids[count.index]}"
}



variable "vpc_cidr" {
  description = "Choose CIDR for VPC"
  type        = "string"
  default     = "10.0.0.0/16"
}

variable "region" {
  description = "Choose region for your stack"
  type        = "string"
  default     = "ap-south-1"
}
variable "web_instance_count" {
  description = "Choose instance count"
  type        = "string"
  default     = "2"
}

variable "web_amis" {
  type = "map"
  default = {
    ap-south-1     = "ami-0d2692b6acea72ee6"
    ap-southeast-1 = "ami-01f7527546b557442"
  }
}


resource "aws_security_group" "web" {
  name   = "web_security"
  vpc_id = "${aws_vpc.my_vpc.id}"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
