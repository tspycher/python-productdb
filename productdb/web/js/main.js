var app =  angular.module('myApp',[]);

app.controller('ProductsController', function($scope, $http){

    $scope.name = "Coder01";
    $scope.page = 1;

    init();

    $scope.nextPage = function() {
        $scope.page++;
        getData();
    }
    $scope.previousPage = function() {
        $scope.page--;
        getData();
    }

    function init() {
        $scope.page = 1;
        getData();
    }

    function getData() {
        $http.get('http://localhost:5000/product?page='+$scope.page).
            success(function(data) {
                $scope.products = data._items;
                console.log($scope.products);
            }
        );
    }
});



