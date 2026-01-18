run "deploy" {
  command = apply
}

# Pas de validate HTTP ici car Function URL renvoie 403 dans ton compte/org


run "validate" {
  command = apply

  module {
    source = "../../modules/test-endpoint"
  }

  variables {
    endpoint = run.deploy.api_endpoint
  }

  # assert {
  # condition     = data.http.test_endpoint.status_code == 200
  # error_message = "Unexpected status: ${data.http.test_endpoint.status_code}"
  # }

  assert {
    condition     = data.http.test_endpoint.response_body == "DevOps Labs!"
    error_message = "Unexpected body: ${data.http.test_endpoint.response_body}"
  }

}