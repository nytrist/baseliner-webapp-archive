		//set correct url to pass to api
		var thisURL = window.location.protocol + "//" + window.location.host + window.location.pathname
		var apihost = 'japan-api.soil.watch'; //local address of api - stations
		var apiURL = window.location.protocol + "//" + apihost + window.location.pathname

		//call api
			httpGetAsync(apiURL, function(response) {
					var stations = JSON.parse(response);
					appendData(stations);
				}
			)
