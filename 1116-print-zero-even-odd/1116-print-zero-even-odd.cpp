class ZeroEvenOdd {
private:
    int n;

    mutex mtx;
    condition_variable cv;

    int current = 1;

    // 0 = zero
    // 1 = odd
    // 2 = even
    int turn = 0;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(function<void(int)> printNumber) {
        for(int i = 0; i < n; i++){
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){
                return turn == 0;
            });
            printNumber(0);
            if(current%2 == 1){
                turn = 1;
            }else{
                turn = 2;
            }
            cv.notify_all();
        }
    }

    void even(function<void(int)> printNumber) {
        for(int i = 2;i<=n; i+=2){
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){
                return turn == 2;
            });
            printNumber(current);
            current++;
            turn = 0;
            cv.notify_all();
        }
    }

    void odd(function<void(int)> printNumber) {
        for(int i = 1;i<=n; i+=2){
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){
                return turn == 1;
            });
            printNumber(current);
            current++;
            turn = 0;
            cv.notify_all();
        }
    }
};