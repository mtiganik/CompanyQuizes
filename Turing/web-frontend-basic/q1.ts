class TuringQueue<T> {
    private data = [];
    push = (item: T) => this.data.push(item);
    pop = (): T => this.data.shift();
}

const TuringQueue = new TuringQueue<number>();
TuringQueue.push(0);
TuringQueue.push("1")
console.log(TuringQueue)