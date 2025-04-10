/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let newFlowersPlanted = 0; 
    for (let i = 0; i < flowerbed.length; i++) {
        const cantPlant = (flowerbed[i] === 1) || ((i === 0 ? false : flowerbed[i-1] === 1 )) || ((i === flowerbed.length - 1 ? false : flowerbed[i+1] === 1)); 

        if(!cantPlant) {
            flowerbed[i] = 1; 
            newFlowersPlanted++;
        }
    }

    return newFlowersPlanted >= n; 
};