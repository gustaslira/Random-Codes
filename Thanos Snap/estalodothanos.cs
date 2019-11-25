using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ThanosSnap {
  class MainClass {
    static void Main (string[] args) {

      var rand = new Random();
      for (int i = 0; i < 1; i++){

        int snap = rand.Next(0,2);

        if (snap == 1){
            Console.WriteLine("You were spared by Thanos.");
        }

        else{
            Console.WriteLine("You were slain by Thanos, for the good of the Universe.");
        }

      }
    }
  }
}
