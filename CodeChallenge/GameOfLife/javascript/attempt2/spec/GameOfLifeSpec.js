describe("Player", function() {
  var Player = require('../lib/GameOfLife.js');

  it("should be able to play a Song", function() {
    expect(player.currentlyPlayingSong).toEqual(song);

    expect(player).toBePlaying(song);
  });

});
