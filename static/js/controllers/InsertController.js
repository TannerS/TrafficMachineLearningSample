angular.module('H3', [])
    .controller('insert_controller', function ($scope, $http) {

    $scope.insert = function() {
        $http({
            url : "/addData",
            method : "POST",
            params : {
                road_id : $scope.road_id,
                direction : $scope.direction,
                day_of_week : $scope.day_of_week,
                time_of_day : $scope.time_of_day,
                traffic_status : $scope.traffic_status
            }
        }).then(function (response) {
            // $scope.show_inserted = true;

            console.log("DEBUG:" + response);
            console.log("DEBUG:" + JSON.stringify(response));

            $scope.result = response["data"]
        });

        $scope.traffic_status = "";
        $scope.time_of_day = "";
        $scope.day_of_week = "";
        $scope.direction = "";
        $scope.road_id = "";;
    };
});
