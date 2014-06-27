"use strict";

var telekomCtrls = angular.module('telekomCtrls', []);

telekomCtrls.controller('rootCtrl', ['$scope', 'sipSrv',
	function($scope, sipSrv) {

	// modal for SIP login
	$('#loginModal').modal('show');

	// function to login in kamailio
	$scope.submitLogin = function() {
		var sip = new sipSrv($scope.username, $scope.password);
		sip.login();

		window.sip = sip;
	};
}]);
