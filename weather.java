public class MainActivity extends AppCompatActivity {

  private static final String TAG = "MainActivity";

  private TextView mTemperatureTextView;
  private TextView mConditionTextView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    mTemperatureTextView = findViewById(R.id.temperature_text_view);
    mConditionTextView = findViewById(R.id.condition_text_view);

    Button button = findViewById(R.id.button);
    button.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View view) {
        fetchWeather();
      }
    });
  }

  private void fetchWeather() {
    String location = "Seattle, WA"; // replace with user-entered location
    String url = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=YOUR_API_KEY";
    Request request = new Request.Builder()
        .url(url)
        .build();

    OkHttpClient client = new OkHttpClient();
    client.newCall(request).enqueue(new Callback() {
      @Override
      public void onFailure(@NotNull Call call, @NotNull IOException e) {
        e.printStackTrace();
      }

      @
