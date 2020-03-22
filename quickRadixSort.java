package Sorts;
import java.io.*; 
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class quickRadixSort {
	// Radix sort Java implementation 
	  
	    // A utility function to get maximum value in arr[] 
	    static int getMax(int arr[], int n) 
	    { 
	        int mx = arr[0]; 
	        for (int i = 1; i < n; i++) 
	            if (arr[i] > mx) 
	                mx = arr[i]; 
	        return mx; 
	    } 
	  
	    // A function to do counting sort of arr[] according to 
	    // the digit represented by exp. 
	    static void countSort(int arr[], int n, int exp) 
	    { 
	        int output[] = new int[n]; // output array 
	        int i; 
	        int count[] = new int[10]; 
	        Arrays.fill(count,0); 
	  
	        // Store count of occurrences in count[] 
	        for (i = 0; i < n; i++) 
	            count[ (arr[i]/exp)%10 ]++; 
	  
	        // Change count[i] so that count[i] now contains 
	        // actual position of this digit in output[] 
	        for (i = 1; i < 10; i++) 
	            count[i] += count[i - 1]; 
	  
	        // Build the output array 
	        for (i = n - 1; i >= 0; i--) 
	        { 
	            output[count[ (arr[i]/exp)%10 ] - 1] = arr[i]; 
	            count[ (arr[i]/exp)%10 ]--; 
	        } 
	  
	        // Copy the output array to arr[], so that arr[] now 
	        // contains sorted numbers according to curent digit 
	        for (i = 0; i < n; i++) 
	            arr[i] = output[i]; 
	    } 
	  
	    // The main function to that sorts arr[] of size n using 
	    // Radix Sort 
	    static void radixsort(int arr[], int n) 
	    { 
	        // Find the maximum number to know number of digits 
	        int m = getMax(arr, n); 
	  
	        // Do counting sort for every digit. Note that instead 
	        // of passing digit number, exp is passed. exp is 10^i 
	        // where i is current digit number 
	        for (int exp = 1; m/exp > 0; exp *= 10) 
	            countSort(arr, n, exp); 
	    } 
	  
	    // A utility function to print an array 
	    static void print(int arr[], int n) 
	    { 
	        for (int i=0; i<n; i++) 
	            System.out.print(arr[i]+" "); 
	    } 
	    
	    public static void quickSort(int[] arr) {	    	
	    	quickSort(arr, 0, arr.length - 1);
	    }
	    private static void quickSort(int[] a, int lo, int hi) {
		    if (hi <= lo) return;
		    int j = partition(a, lo, hi); // Partition (see page 291).
		    quickSort(a, lo, j-1);
		    // Sort left part a[lo .. j-1].
		    quickSort(a, j+1, hi);
		    // Sort right part a[j+1 .. hi].
	    }
	    
	    private static int partition(int[] arr, int lo, int hi) { 
	    	int i = lo, j = hi+1;
	    	int v = arr[lo];
		    while (true)
		    { // Scan right, scan left, check for scan complete, and exchange.
			    while (arr[++i] < v) if (i == hi) break;
			    while (v < arr[--j]) if (j == lo) break;
			    if (i >= j) break;
			    int temp = arr[i];
			    arr[i] = arr[j];
			    arr[j] = temp;
		    }
		    int temp = arr[lo];
		    arr[lo] = arr[j];
		    arr[j] = temp;
		    // Put v = a[j] into position
		    return j;
		    // with a[lo..j-1] <= a[j] <= a[j+1..hi].
	    }
	    
	    
	    
	    
	    
	    
	  
	    
	    // random shuffle function
	    static void shuffleArray(int[] ar)
	    {
	      
	      Random rnd = ThreadLocalRandom.current();
	      for (int i = ar.length - 1; i > 0; i--)
	      {
	        int index = rnd.nextInt(i + 1);
	        // Simple swap
	        int a = ar[index];
	        ar[index] = ar[i];
	        ar[i] = a;
	      }
	    }
	  
	    /*Driver function to check for above function*/
	    public static void main (String[] args) 
	    { 
	    	Random r = new Random();
	    	int low = 0;
	    	int high = 1000000;
	        int[] arr = new int[1000000];
	        for (int i = 0; i < arr.length; i++) {
	        	arr[i] = r.nextInt(high-low) + low;
	        }
	        int n = arr.length; 
	        long start = System.nanoTime();
	        radixsort(arr, n);
	        System.out.print(System.nanoTime()-start);
	        System.out.println();
	        shuffleArray(arr);
	        start = System.nanoTime();
	        quickSort(arr);
	        System.out.print(System.nanoTime()-start);
	    }  
	
}
