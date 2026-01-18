provider "aws" {
  region = "us-east-2"
}

module "function" {
  source  = "brikis98/devops/book//modules/lambda"
  version = "1.0.0"

  name = var.name

  src_dir = "${path.module}/src"
  runtime = "nodejs20.x"
  handler = "index.handler"

  memory_size = 128
  timeout     = 5

  create_url = true


  environment_variables = {
    NODE_ENV = "production"
  }
}

module "test_endpoint" {
  source = "../../modules/test-endpoint"

  name     = var.name
  endpoint = module.function.function_url

  depends_on = [
  time_sleep.wait_for_url_permission,
  aws_lambda_permission.allow_public_invoke_url
  ]

}


resource "aws_lambda_permission" "allow_public_invoke_url" {
  statement_id           = "AllowPublicInvokeFunctionUrl"
  action                 = "lambda:InvokeFunctionUrl"
  function_name          = module.function.function_name
  principal              = "*"
  function_url_auth_type = "NONE"

  depends_on = [module.function]
}

resource "time_sleep" "wait_for_url_permission" {
  create_duration = "20s"
  depends_on = [
    module.function,
    aws_lambda_permission.allow_public_invoke_url
  ]
}
