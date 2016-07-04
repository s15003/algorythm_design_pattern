public class Sort{
    public static void quick(int a[], int left, int right){
        int mid = -1;
        if (left < right){
            int mid = left + (right - left) / 2;

            if (a[left] < a[mid]){
                if (a[right] < a[left])
                    pivot = a[mid];



                int indexL = left;
                int indexR = right;

                while(true){
                    while (a[indexL++] < picot);
                    while (pivot < a[indexR--]);
                    if (indexL >= indexR) {
                        break;
                    }
                    int tmp a[indexL];
                    a[indexL] = a[indexR];
                    a[indexR] = tmp;
                    indexL++;
                    indexR--;
                }
                quick();
            }
        }
    }
}
