class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        const len:number = board[0].length;
        const rowSets: Array<Set<string>> = Array.from({length:len},() => new Set());
        const colSets: Array<Set<string>> = Array.from({length:len},() => new Set());
        const subgridSets: Array<Set<string>> = Array.from({length:len},() => new Set());
        // build subgrid map
        const subgridMap = [[0,1,2],[3,4,5],[6,7,8]];

        for(let row:number = 0; row < len; row++){
            for (let col:number = 0; col < len; col++){
                const char = board[row][col];
                if(char!= "."){
                    const subgridIdx = subgridMap[Math.floor(row/3)][Math.floor(col/3)];
                    if(rowSets[row].has(char) || colSets[col].has(char) || subgridSets[subgridIdx].has(char))
                        return false;
                    rowSets[row].add(char);
                    colSets[col].add(char);
                    subgridSets[subgridIdx].add(char);
                }
            }
        }

        return true;
    }
}
