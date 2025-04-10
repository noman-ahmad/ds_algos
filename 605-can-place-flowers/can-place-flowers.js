/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let newFlowersPlanted = 0; 
    for (let i = 0; i < flowerbed.length; i++) {
        const alreadyPlanted = flowerbed[i] === 1; 
        const leftPlanted = (i === 0 ? false : flowerbed[i-1] === 1 ); 
        const rightPlanted = (i === flowerbed.length - 1 ? false : flowerbed[i+1] === 1); 

        if(!(alreadyPlanted || rightPlanted || leftPlanted)) {
            flowerbed[i] = 1; 
            newFlowersPlanted++;
        }
    }

    return newFlowersPlanted >= n; 
};