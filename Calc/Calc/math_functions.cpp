

extern "C" __declspec(dllexport) int add(int a, int b) {
    return a + b;
}


extern "C" __declspec(dllexport) int subtract(int a, int b) {
    return a - b;
}


extern "C" __declspec(dllexport)int multiply(int a, int b) {
    return a * b;
}
