output "api_endpoint" {
  value = "${aws_api_gateway_stage.stage.invoke_url}/detect"
}

output "lambda_function_name" {
  value = aws_lambda_function.image_recognition.function_name
}