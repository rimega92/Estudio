public class ejemplo {
    public static void main(String[] args) {

        System.out.println("Histograma");

        int [] myArray = {1,2,1,3,3,1,2,1,5,1};
        String [] results = new String[5];
        for (int i = 0; i < results.length; i++){
            results[i] = "";
        }
        for (int value : myArray) {
            results[value - 1] = results[value - 1] + "*";
        }
        for (int i = 0; i < results.length; i++){
            System.out.println( (i + 1) + ": " + results[i]);
        }

        System.out.println("Fin Histograma\n");


        System.out.println("Matriz Diagonal X");

        int n=5;
        int diagonalPrincipalIndex = 0;
        int diagonalSecundariaIndex = n-1;

        if (n == 0){
            System.out.println("ERROR");
        }else{
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    if (j == diagonalPrincipalIndex || j == diagonalSecundariaIndex){
                        System.out.print("X");
                    } else{
                        System.out.print("_");
                    }
                }
                System.out.print("\n");
                diagonalPrincipalIndex = diagonalPrincipalIndex + 1;
                diagonalSecundariaIndex = diagonalSecundariaIndex - 1;
            }
        }

        System.out.println("Fin Matriz Diagonal X\n");


        System.out.println("Numero que tiene mas ocurrencias y cuantas");

        int[] myArray2 = {1,2,2,4,5,6,7,8,8,8,};
        int longest = 0;
        int number = 0;
        int longest1 = 0;
        int number1 = 0;
        for (int i = 0; i < myArray2.length; i++){
            number = myArray2[i];
            for (int j = 0; j< myArray2.length; j++){
                if (number == myArray2[j]){
                    longest += 1;
                }
            }
            if (longest > longest1){
                longest1 = longest;
                number1 = number;
            }
            longest = 0;
        }
        System.out.println("Longest:" + longest1);
        System.out.println("Number:" + number1);

        System.out.println("Fin Numero que tiene mas ocurrencias y cuantas\n");


        System.out.println("Numero mayor de Array");

        int[] myArray3 = {13,2,4,35,1};
        int mayor = 0;
        for (int i = 0; i < myArray3.length; i++) {
            if (mayor < myArray3[i]){
                mayor = myArray3[i];
            }
        }
        System.out.println(mayor);

        System.out.println("Fin Numero mayor de Array\n");


        System.out.println("Otro");
    }
}
