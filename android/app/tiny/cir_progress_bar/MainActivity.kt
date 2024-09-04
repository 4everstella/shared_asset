package com.bd.ui_cir_bar

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.content.Intent
import android.widget.Button

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val launchButton = findViewById<Button>(R.id.launchButton)
        launchButton.setOnClickListener {
            val intent = Intent(this, DummyFrameActivity::class.java)
            startActivity(intent)
        }
    }
}
