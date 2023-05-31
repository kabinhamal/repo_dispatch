(function executeRule(current, previous /*null when async*/) {

    var url = "https://api.github.com/repos/BAC/test-repo/dispatches";
    var accessToken = "<GitHub Personal Access Token>";
  
    var payload = {
      event_type: "my_event_type",
      client_payload: {
        appID: "app",
        region: "eus"
      }
    };
  
    var headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + accessToken
    };
  
    var response = new sn_ws.RESTMessageV2();
    response.setEndpoint(url);
    response.setHttpMethod("POST");
    response.setRequestHeader("Accept", "application/vnd.github.v3+json");
    response.setRequestBody(JSON.stringify(payload));
    response.setRequestHeader("Authorization", "Bearer " + accessToken);
  
    var httpResponse = response.execute();
    var responseBody = httpResponse.getBody();
    
    gs.info("Response Body: " + responseBody);
    
  })(current, previous);
  