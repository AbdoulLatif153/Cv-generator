import React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import { CssBaseline, Container } from '@mui/material';
import theme from './styles/theme';
import CVForm from './components/CVForm';

function App() {
  const handleSubmit = (data) => {
    console.log('CV Data:', data);
    // Ici nous ajouterons l'appel API plus tard
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ mt: 4 }}>
        <CVForm onSubmit={handleSubmit} />
      </Container>
    </ThemeProvider>
  );
}

export default App;
