```mermaid
flowchart TD
    A([Start]) --> B[/Enter patient name and category/]
    B --> C[/Enter consultation, diagnostic, treatment charges/]
    C --> D{Are all charges >= 0?}
    D -- No --> E[/Display Invalid Charges/]
    E --> Z([Stop])
    D -- Yes --> F[Calculate Total Bill]
    F --> G{Senior Citizen?}
    G -- Yes --> H[Apply 10% Concession]
    G -- No --> I[Concession = 0]
    H --> J[Calculate Final Bill]
    I --> J
    J --> K{Final Bill >= 5000?}
    K -- Yes --> L[High-Payment Patient]
    K -- No --> M[Regular-Payment Patient]
    L --> N[/Display Bill Details/]
    M --> N
    N --> Z
```
