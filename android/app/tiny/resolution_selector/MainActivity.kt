package com.bd.arr_ui

import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.RadioButton
import android.widget.RadioGroup
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var resolutionRadioGroup: RadioGroup
    private lateinit var applyButton: Button
    private var selectedResolution: String = "360p" // Default resolution

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        resolutionRadioGroup = findViewById(R.id.resolutionRadioGroup)
        applyButton = findViewById(R.id.applyButton)

        // Handle resolution selection
        resolutionRadioGroup.setOnCheckedChangeListener { _, checkedId ->
            val radioButton = findViewById<RadioButton>(checkedId)
            selectedResolution = radioButton.text.toString()
        }

        // Handle apply button click
        applyButton.setOnClickListener {
            Log.d("ResolutionSelector", "Applied Resolution: $selectedResolution")
        }
    }
}

