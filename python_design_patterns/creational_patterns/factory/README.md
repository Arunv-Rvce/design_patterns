# Factory Pattern

- __*Definition*__: Basically factory pattern suggest that whenever there are different entities invoked the client shouldn't care about their implementation, which means based on the client request the factory should be able to return relevant object so client can use it without worrying concerned about their internal logic

Example: In the example code there are basically two stock exchange NSE & BSE whenever the client needs to place a order it will get the method from factory and call place_buy_order()
