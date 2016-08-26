var app =  angular.module('myApp',[]);

app.controller('ProductsController', function($scope, $http){

    $scope.name = "Coder01";
    init();

    function init() {
        $http.get('http://localhost:5000/product').
            success(function(data) {
                $scope.products = data._items;
                console.log($scope.products);
            }
        );
    }
});



