package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import java.util.concurrent.TimeoutException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void click(View view){
        EditText edNumber = findViewById(R.id.textInputEditText);
        TextView text = findViewById(R.id.textView);
        try {
            long time1 = System.currentTimeMillis();
            int number = Integer.parseInt(edNumber.getText().toString());
            if (number % 2 == 0) {
                text.setText((number / 2 + "*" + "2"));
            } else {
                int x = (int) Math.ceil((Math.sqrt(number)));
                while (!(Math.pow((int) Math.sqrt(x * x - number), 2) == x * x - number)) {
                    x += 1;
                    if (System.currentTimeMillis() - time1 > 3000){
                        text.setText("Перевищений час факторизації");
                        throw new Exception("error");
                    }
                }
                int y = (int) Math.sqrt(x * x - number);
                text.setText((x - y) + "*" + (x + y));
            }
        }
        catch (Exception e){
            text.setText("Час факторизації перевищив 3 секунди");
        }
    }
}
