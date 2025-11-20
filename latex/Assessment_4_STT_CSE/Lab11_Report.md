# Lab Assignment 11

## INTRODUCTION
I completed Laboratory Session 11 on events and delegates in C# Windows Forms. The session centered on building a small interactive form and then reasoning through several delegate/event code snippets to understand chaining, thresholds, and nested invocation. In this lab I focused on: (a) wiring custom events between UI controls, (b) extending a basic event with a custom `EventArgs` payload, and (c) demonstrating multicast behavior. After that I manually traced five embedded C# code snippets (Tasks 3–5) and wrote out their outputs with reasoning. I kept the implementation compact and readable rather than over-engineered.

## TOOLS

- OS: Windows 11; Shell: PowerShell 7
- .NET SDK: .NET 8 (meets the “.NET 6 or later” requirement)
- IDE/Editor: Visual Studio 2022 Community
- Git: for version control

![Environment Details](./images/env.png)


## SETUP



1) Install Visual Studio 2022 (Community Edition) with the “.NET desktop development” workload selected.
![Workload Selection](./images/workload.png)

2) Confirm the SDK is on PATH:
   ```pwsh
   dotnet --version
   ```
3) Create a new C# Forms App (or Console App depending upon the task) in Visual Studio and set the Target Framework to .NET 8.0 in project properties.

![Project Target Framework](./images/1.png)

![.NET Version Selection](./images/net8.png)



## METHODOLOGY AND EXECUTION

I created the form with two buttons (`btnChangeColor`, `btnChangeText`), one label (`lblMessage` initialized to “Welcome to Events Lab”), and a ComboBox (`cmbColors`) and then added Red, Green, Blue to Items field via Properties window.

![Form Design](./images/2.0.png)


### Part 1 - Basic Custom Events (Color & Text)
In `lab11/1 Form1.cs` I declared two delegates and events:
```csharp
public delegate void ColorChangedHandler(System.Drawing.Color newColor);
public delegate void TextChangedHandler(string newText);
public event ColorChangedHandler ColorChangedEvent;
public event TextChangedHandler TextChangedEvent;
```
I subscribed handlers in the constructor:
```csharp
ColorChangedEvent += UpdateLabelColor;
TextChangedEvent += UpdateLabelText;
```
On the color button click I read the selected ComboBox string, mapped it to a `System.Drawing.Color` with a `switch`, and invoked:
```csharp
ColorChangedEvent?.Invoke(selectedColor); // raises custom event
```
The text button built a timestamp string and invoked:
```csharp
TextChangedEvent?.Invoke(newText);
```
The label foreground and caption updated only through these events - click handlers acted as publishers, subscriber methods performed the UI changes.

(*Insert Screenshot here: code view with constructor plus delegate/event lines, similar to `../images/lab11/part1_code.png`*)
![Code Snippet of Form1.cs for Part 1](./images/2.1.png)

![Code Snippet of Form1.cs for Part 1](./images/2.2.png)

(*Insert Screenshot here: GUI after colour change to Red, similar to `../images/lab11/part1_gui_green.png`*)
![GUI after Color Change](./images/3.png)

![GUI after Text Change](./images/4.png)






### Part 2 - EventArgs + Multicast

I added a class named `ColorEventArgs` to extend the color change event to carry more structured information. 
![ColorEventArgs Class](./images/5.png)


In `ColorEventArgs.cs` I kept it minimalist:
```csharp
public class ColorEventArgs : EventArgs {
    public string ColorName { get; }
    public ColorEventArgs(string colorName) { ColorName = colorName; }
}

![ColorEventArgs Code Snippet](./images/6.0.png)

```
Then in `Form1.cs` I adopted the conventional sender + args pattern:
```csharp
public delegate void ColorChangedHandler(object sender, ColorEventArgs e);
public event ColorChangedHandler ColorChangedEvent;
```
Constructor subscriptions showed multicast:
```csharp
ColorChangedEvent += UpdateLabelColor;
ColorChangedEvent += ShowNotification; // second subscriber
```
Publish side (button click):
```csharp
var args = new ColorEventArgs(selectedColorName);
ColorChangedEvent?.Invoke(this, args);
```
`UpdateLabelColor` mapped the `ColorName` string to a `System.Drawing.Color`; `ShowNotification` popped up a message box confirming the choice. Both ran in order when I clicked the button. This matched the assignment's requirement to demonstrate multiple subscribers.

(*Insert Screenshot here: code view showing delegate, event, and both subscriptions, e.g., `../images/lab11/part2_code_multicast.png`*)

![Code Snippet of Form1.cs for Part 2](./images/6.1.png)

![Code Snippet of Form1.cs for Part 2](./images/6.2.png)


(*Insert Screenshot here: message box after choosing Green, e.g., `../images/lab11/part2_msgbox_blue.png`*)
![GUI and Message Box after Color Change](./images/6.3.png)

### Task 3 - Output Reasoning (Level 0)

Q1 Final Output: `MS:-1`

![Output for Q1](./images/7.png)

Reasoning: The delegate list ended as `[Mul, Sub]` after removing `Add`. Invocation printed `M` then `S`; only the last method’s return (`Sub(2,3) = -1`) surfaced, so the appended result became `:-1`.

Q2 Final Output: `I5 D4 F4`

![Output for Q2](./images/8.png)

Reasoning: `Inc` bumped `val` from 3 to 5 and printed `I5 `; `Dec` lowered it to 4 and printed `D4 `; afterward printing `F4` reflected the final value (multicast with `ref` propagates changes across calls).

### Task 4 - Output Reasoning (Level 1)
Q1 Final Output: `>1>2[M2]>3[L3](Reset)>4[M4]{Alert}>5>6[M6][L6](Reset)`

![Output for Q1 Level 1](./images/9.png)

Reasoning: Each increment printed `>value`. Milestones at even values produced `[Mvalue]` and added `{Alert}` specifically at 4. Limits at multiples of 3 produced `[Lvalue](Reset)` via two subscribers. Tracing values 1 through 6 gave the sequence above.


Q2 Final Output:
```
Temperature changed from 30°C to 46°C
 Warning: Sudden change detected!
Temperature changed from 46°C to 52°C
```

![Output for Q2 Level 1](./images/10.png)

Reasoning: Only jumps greater than 5 fired the event. 25→28 and 28→30 were ignored. 30→46 fired (Δ16) printing the line plus a warning because Δ>10. 46→52 fired (Δ6) printing the line; Δ6 was not >10 so no warning.





### Task 5 - Output Reasoning (Level 2)

Q1 Final Output: `[Start]{Ping}(Nested)[Start]{Pong}(Nested)[End][End]`

![Output for Q1 Level 2](./images/11.png)

Reasoning: Outer trigger printed `[Start]`, then two subscribers: `{Ping}` and `(Nested)`. The second re-triggered with `Pong`, producing a nested `[Start]`, then `{Pong}` and `(Nested)` again; no further recursion because message changed. Each trigger closed with `[End]` yielding two `[End]` tokens.


Q2 Final Output: `[Check]{High}[Check][Done](Alert)[Done]`

![Output for Q2 Level 2](./images/12.png)

Reasoning: First `[Check]` from the 80 call. Threshold passed so subscriber 1 printed `{High}` then internally called `Check(30)` which printed `[Check][Done]` (no event). Subscriber 2 printed `(Alert)`. Original call then printed its closing `[Done]`.

## CONCLUSION
In this lab I built a Windows Forms example that used custom delegates and events to drive UI updates rather than direct control manipulation inside button handlers. I then extended the design using a custom `ColorEventArgs` and demonstrated multicast events by wiring both a label update and a message box to the same publisher. Tracing the five reasoning snippets reinforced how multicast delegates preserve invocation order, how only the last return value is kept, how conditional event firing depends on data thresholds, and how nested event triggers can produce interleaved output. Overall the exercise strengthened my comfort with the publisher–subscriber pattern in C# and clarified practical details like using `?.Invoke`, passing `ref` parameters through multicast delegates, and composing EventArgs for extensibility without changing event signatures.

## REFERENCES
- Lecture 12 slides (course material)
- Microsoft Learn: Delegates and Events in C#
- C# Delegates Overview (official docs)
- Windows Forms Events Guide (Microsoft docs)
- General event-driven programming concepts (standard references)

