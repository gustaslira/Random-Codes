import java.util.Random;

class Main {
  public static void main(String[] args) {
    
    Random rand = new Random();
    
    int n = rand.nextInt(2);
    n += 1;
    if (n == 1) {
      System.out.print("You were spared by Thanos.");
    } else {
      System.out.print("You were slain by Thanos, for the good of the Universe.");
    }    
    
    
  }
}