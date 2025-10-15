function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) {
      return i + 1;
    }
  }
  return -1;
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i = 0; i < uiBHK.length; i++) {
    if (uiBHK[i].checked) {
      return i + 1;
    }
  }
  return -1;
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");

  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  
  var url = "https://bangalore-realestate-pricepredictor.onrender.com/predict_home_price";

  $.post(url, {
    total_sqft: parseFloat(sqft.value),
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function (data, status) {
    console.log("Response:", data);
    if (data && data.estimated_price) {
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    } else {
      estPrice.innerHTML = "<h2>Could not fetch price</h2>";
    }
  }).fail(function () {
    estPrice.innerHTML = "<h2>Server Error - Try again</h2>";
  });
}

function onPageLoad() {
  console.log("Document loaded");

  
  var url = "https://bangalore-realestate-pricepredictor.onrender.com/get_location_names";

  $.get(url, function (data, status) {
    console.log("Got response for get_location_names request:", data);
    if (data && data.locations) {
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in data.locations) {
        var opt = new Option(data.locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  }).fail(function () {
    console.log("Error loading locations from backend");
  });
}

window.onload = onPageLoad;
