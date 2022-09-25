package week5;
import java.awt.Color;

import javax.swing.*;

public class Work1 {
    public static void main(String[] args) {
        JFrame window;
        JButton b = new JButton("hungry");
        window = new JFrame();
        window.setTitle("Java");
        b.setBackground(Color.GREEN);
        window.add(b);
        b.setBounds(375, 400, 75, 40);
        window.setSize(500, 500);
        window.setLayout(null);


        window.setVisible(true);
    }
}
