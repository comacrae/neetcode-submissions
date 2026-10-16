class MinStack {
    private st: Array<number>;
    private minSt :Array<number>;
    constructor() {
        this.st = new Array<number>();
        this.minSt = new Array<number>();
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val: number): void {
        //push val onto stack
        this.st.push(val);
        // if minSt is empty, push val onto minSt
        if (this.minSt.length === 0) this.minSt.push(val);
        // else if val <= top of minSt, push onto minSt
        else{
            const minStTop = this.minSt[this.minSt.length - 1];
            if (val <= minStTop) this.minSt.push(val);
        }
        return;
    }

    /**
     * @return {void}
     */
    pop(): void {
        //remove top of stack
        const topVal = this.st.pop();
        // if value == top of minStack, pop minStack as well
        if(topVal === this.minSt[this.minSt.length - 1])
            this.minSt.pop();
        
        return;
    }

    /**
     * @return {number}
     */
    top(): number {
        //get last element in stack
        return this.st[this.st.length-1];
    }

    /**
     * @return {number}
     */
    getMin(): number {
        //get last element in minSt
        return this.minSt[this.minSt.length - 1];
    }
}
