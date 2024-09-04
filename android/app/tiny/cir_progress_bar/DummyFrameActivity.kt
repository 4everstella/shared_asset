package com.bd.ui_cir_bar

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.os.Handler
import android.os.Looper
import android.widget.ProgressBar

class DummyFrameActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dummy_frame)

        // Start the progress animation
        val progressBar = findViewById<ProgressBar>(R.id.progressBar)
        progressBar.max = 100

        // Simulate a duration of 5 seconds
        val duration = 2000
        val handler = Handler(Looper.getMainLooper())
        handler.postDelayed({
            // Launch the target application
            val launchIntent = packageManager.getLaunchIntentForPackage("com.android.chrome")
            if (launchIntent != null) {
                startActivity(launchIntent)
            }
            finish()
        }, duration.toLong())

        // Update the progress bar
        Thread {
            var progress = 0
            while (progress < 100) {
                Thread.sleep((duration / 100).toLong())
                progress++
                handler.post {
                    progressBar.progress = progress
                }
            }
        }.start()
    }
}
