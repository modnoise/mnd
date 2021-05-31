package com.example.lab2a;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import static java.lang.Math.random;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    public void Start(View view) {
        TextView res = findViewById(R.id.textView6);
        int count_answers = 0;
        for (int i = 0; i < 1000; i++) {

            long start = System.currentTimeMillis();

            double[] data = {0.01, 5, 1000};
            data[0] = random()*0.3;
            data[2] = random()*1000;

            double stage = 4;
            double W1 = 0;
            double W2 = 0;

            double[][] points = {{0.0, 6.0}, {1.0, 5.0}, {3.0, 3.0}, {2.0, 4.0}};

            int count = 0;
            int succ = 0;
            int curP = -1;
            int hod = 0;
            while (count <= data[2]) {
                if (succ >= 4) {
                    break;
                }

                curP = hod % 4;
                hod++;

                double test = W1 * points[curP][0] + W2 * points[curP][1];

                if (((curP < 2) && test >= stage) || ((curP >= 2) && test < stage)) {
                    succ++;
                    continue;
                } else {
                    succ = 0;
                }

                double delta = stage - test;

                W1 += delta * points[curP][0] * data[0];
                W2 += delta * points[curP][1] * data[0];

                W1 = Math.ceil(W1 * Math.pow(10, 7)) / Math.pow(10, 7);
                W2 = Math.ceil(W2 * Math.pow(10, 7)) / Math.pow(10, 7);

                if (System.currentTimeMillis() - start >= data[1]) {
                    break;
                }

                count++;
            }

            if(Double.isNaN(W1)){
                System.out.println(" ");
            }
            else{
                count_answers = count_answers + 1;
            }
        }
        res.setText("Корені були знайдені: " + count_answers + " раз");
    }
}
