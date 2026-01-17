output "function_name" {
  value       = module.function.function_name
  description = "Lambda function name"
}

output "api_endpoint" {
  value       = module.function.function_url
  description = "Function URL used as endpoint"
}
