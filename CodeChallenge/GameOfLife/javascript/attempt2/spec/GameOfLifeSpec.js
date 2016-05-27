describe("GameOfLifeSpec", function() {
  var GameOfLife = require('../lib/GameOfLife.js');
  var gameOfLife;

  it("should be able to compute next version of grid", function() {
    gameOfLife = new GameOfLife([    
            [ false,  false, false, false, false] ,
            [ false,   true,  true,  true, false] ,
            [ false,   true,  true,  true, false] ,
            [ false,  false, false, false, false] 
            ]);

    expectedOuput = [
            [ false,  false,  true, false, false] ,
            [ false,   true, false,  true, false] ,
            [ false,   true, false,  true, false] ,
            [ false,  false,  true, false, false] 
    ];

    expect(gameOfLife.compute_next_board()).toEqual(expectedOuput);

  });

});

