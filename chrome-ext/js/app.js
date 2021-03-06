angular.module('myApp', ['ngRoute'])


// angular.module(...)
// // ...
// .config(function($routeProvider) {
//   $routeProvider
//     .when('/', {
//       templateUrl: 'templates/home.html',
//       controller: 'MainCtrl'
//     })
//     .when('/settings', {
//       templateUrl: 'templates/settings.html',
//       controller: 'SettingsCtrl'
//     })
//     .otherwise({redirectTo: '/'});
// })

// .factory('UserService', function() {
//   var defaults = {
//     location: 'autoip'
//   };

//   var service = {
//     user: {},
//     save: function() {
//       sessionStorage.presently =
//         angular.toJson(service.user);
//     },
//     restore: function() {
//       // Pull from sessionStorage
//       service.user =
//         angular.fromJson(sessionStorage.presently) || defaults

//       return service.user;
//     }
//   };
//   // Immediately call restore from the session storage
//   // so we have our user data available immediately
//   service.restore();
//   return service;
// })


.controller('SettingsCtrl', ['$scope', function ($scope,UserService) {

    $scope.user = UserService.user;
    $scope.save = function() {
      UserService.save();
    }
}])



.provider('Weather', function() {
  var apiKey = "52915fa2e8e5e469";
  this.getUrl = function(type, ext) {
  return "http://api.wunderground.com/api/" +
    this.apiKey + "/" + type + "/q/" +
    ext + '.json';
	};
  this.setApiKey = function(key) {
    if (key) this.apiKey = key;
  };

  this.getUrl = function  (type,ext) {
  	return "http://api.wunderground.com/api/" +
    this.apiKey + "/" + type + "/q/" +
    ext + '.json';
  }

  this.$get = function($q, $http) {
  var self = this;
  return {
    getWeatherForecast: function(city) {
      var d = $q.defer();
      $http({
        method: 'GET',
        url: self.getUrl("forecast", city),
        cache: true
      }).success(function(data) {
        // The wunderground API returns the
        // object that nests the forecasts inside
        // the forecast.simpleforecast key
        d.resolve(data.forecast.simpleforecast);
      }).error(function(err) {
        d.reject(err);
      });
      return d.promise;
	    }
	  }
	}
})



.config(function(WeatherProvider) {
  WeatherProvider.setApiKey('52915fa2e8e5e469');
})

.controller('MainCtrl', function($scope, $timeout,Weather,UserService) {
  // Build the date object
  $scope.date = {};
  $scope.weather = {}
  // Update function
  $scope.user = UserService.user;
    Weather.getWeatherForecast($scope.user.location)
    .then(function(data) {
      $scope.weather.forecast = data;
    });
  Weather.getWeatherForecast("IN/Bhubaneswar")
    .then(function(data) {
      $scope.weather.forecast = data;
    });

  var updateTime = function() {
    $scope.date.raw = new Date();
    $timeout(updateTime, 1000);
  }

  // Kick off the update function
  updateTime();


});


.directive('autoFill', function($timeout) {
  return {
    restrict: 'EA',
    scope: {
      autoFill: '&',
      ngModel: '='
    },
    compile: function(tEle, tAttrs) {
      // Our compile function
      return function(scope, ele, attrs, ctrl) {
        // Our link function
      }
    }
  }
})
