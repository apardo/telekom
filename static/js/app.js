var telekom = angular.module('telekom', [
	'ngRoute',
	'telekomCtrls',
]);

telekom.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: '/static/js/views/root.html',
        controller: 'rootCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
