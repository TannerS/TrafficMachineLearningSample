angular.module('H3', [])
    .controller('predict_controller', function ($scope, $http) {

        $scope.predict = "";
        $scope.show_result = false;

        $scope.prediction = function() {
            $http({
                url : "/predict",
                method : "POST",
                params : {
                    road_id : $scope.road_id,
                    direction : $scope.direction,
                    day_of_week : $scope.day_of_week,
                    time_of_day : $scope.time_of_day
                }
            }).then(function (response) {
                $scope.show_result = true;
                $scope.predict = response["data"]["result"]
            });
        };
});