#include<iostream>
using namespace std;

class Solution {
  public:
    int H[501];   // Heap array (constraint n <= 500)
    int s = -1;   // Current index (heap size - 1)

    // 1. Return parent index
    int parent(int i) {
        return (i - 1) / 2;
    }

    // 2. Return left child index
    int leftChild(int i) {
        return 2 * i + 1;
    }

    // 3. Return right child index
    int rightChild(int i) {
        return 2 * i + 2;
    }

    // 4. Shift up to maintain max-heap property
    void shiftUp(int i) {
        while (i > 0 && H[parent(i)] < H[i]) {
            swap(H[i], H[parent(i)]);
            i = parent(i);
        }
    }

    // 5. Shift down to maintain max-heap property
    void shiftDown(int i) {
        int maxIndex = i;
        int l = leftChild(i);
        int r = rightChild(i);

        if (l <= s && H[l] > H[maxIndex])
            maxIndex = l;

        if (r <= s && H[r] > H[maxIndex])
            maxIndex = r;

        if (i != maxIndex) {
            swap(H[i], H[maxIndex]);
            shiftDown(maxIndex);
        }
    }

    // Extract maximum element
    int extractMax() {
        if (s < 0)
            return -1;

        int maxElement = H[0];
        H[0] = H[s];
        s--;

        shiftDown(0);

        return maxElement;
    }
};