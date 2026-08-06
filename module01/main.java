public class Main {
    public static void main(String[] args){
        Main m = new Main();
        System.out.println(m.add_numbers(5,6));
        System.out.println(m.add_numbers(5,6,11));
    }

    public int add_numbers(int a, int b){
        return a + b;
    }

    public int add_numbers(int a, int b, int c){
        return a + b + c;
    }
}