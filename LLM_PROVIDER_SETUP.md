# LLM Provider Configuration

The Brag Document Generator now supports multiple LLM providers: **Gemini** and **Groq**.

## Features Added

### 1. Dynamic Provider Selection
- Users can choose between Gemini and Groq providers
- API key input for authentication
- Dynamic model loading based on selected provider

### 2. Model Selection
- Automatically fetches available models from the selected provider's API
- Models are loaded dynamically when provider and API key are provided
- Supports all available models from both providers

### 3. Enhanced Form Interface
- New dropdown for LLM provider selection
- Secure API key input field (password type)
- Dynamic model dropdown that updates based on provider selection

## Supported Providers

### Gemini
- **API Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models`
- **Authentication**: API key via `x-goog-api-key` header
- **Models**: Automatically fetches all models that support `generateContent`

### Groq
- **API Endpoint**: `https://api.groq.com/openai/v1/models`
- **Authentication**: Bearer token via `Authorization` header
- **Models**: Fetches all available models from the API

## How It Works

1. **Provider Selection**: User selects either Gemini or Groq from dropdown
2. **API Key Input**: User enters their API key for the selected provider
3. **Model Loading**: System automatically fetches available models via API
4. **Model Selection**: User chooses from the dynamically loaded model list
5. **Document Generation**: System uses the selected provider, API key, and model for generation

## API Endpoints

### `/get-models/` (POST)
Fetches available models for a given provider and API key.

**Request Body:**
```json
{
  "provider": "gemini|groq",
  "api_key": "your-api-key"
}
```

**Response:**
```json
{
  "models": [
    {
      "id": "model-id",
      "name": "Model Display Name"
    }
  ]
}
```

## Technical Implementation

### Backend Changes
- Added `get_available_models()` function in `utils.py`
- Updated `generate_brag_document()` to accept provider parameters
- Added new `/get-models/` endpoint in views
- Added support for both `langchain-openai` and `langchain-groq`

### Frontend Changes
- Enhanced form with provider selection and API key input
- Dynamic model loading via JavaScript
- Real-time model list updates based on provider/API key changes
- Improved error handling for API failures

### Dependencies Added
- `langchain-groq`: For Groq LLM integration
- `requests`: For API calls to fetch model lists

## Usage Example

1. Select "Gemini" or "Groq" from the provider dropdown
2. Enter your API key for the selected provider
3. Wait for models to load automatically
4. Select your preferred model from the dropdown
5. Fill in other form fields (employee name, month, Excel file)
6. Generate your brag document

The system will use your selected provider, API key, and model for generating the document.