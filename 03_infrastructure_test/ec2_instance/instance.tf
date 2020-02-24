resource "aws_instance" "example" {
  ami           = "${data.aws_ami.ubuntu.id}"
  instance_type = "${var.instance_type}"

  tags = {
    Name        = "${var.instance_name}"
    Created_By  = "${var.created_by}"
  }
}