interface Theme {
  colors: {
      blue: string;
      gray: string;
      black: string;
      primary: string;
      secondary: string;
      thirdary: string;
      warning: string;
      danger: string;
      shadow_gray: string;
      shadow_blue: string;
      highlights: string;
      background: string;
      text: string;
  };
  font: {
      family: string;
      size: string;
  };
}

// Tema adaptado conforme suas cores e fontes
export const lightTheme: Theme = {
  colors: {
      blue: '#1677ff',
      gray: 'rgba(237, 237, 237, 0.733)',
      black: '#333',
      primary: '#1677ff',
      secondary: '#399E5A',
      thirdary: '#555B6E',
      warning: '#F18805',
      danger: '#F05365',
      shadow_gray: 'rgba(237, 237, 237, 0.733)',
      shadow_blue: '#e6f4ff',
      highlights: '#1677ff',
      background: '#050708',
      text: '#333',
  },
  font: {
      family: 'Roboto, sans-serif',
      size: '16px',
  },
};
// Tema adaptado conforme suas cores e fontes
export const darkTheme: Theme = {
  colors: {
      blue: '#1677ff',
      gray: 'rgba(237, 237, 237, 0.733)',
      black: '#333',
      primary: '#1677ff',
      secondary: '#399E5A',
      thirdary: '#555B6E',
      warning: '#F18805',
      danger: '#F05365',
      shadow_gray: 'rgba(237, 237, 237, 0.733)',
      shadow_blue: '#e6f4ff',
      highlights: '#1677ff',
      background: '#050708',
      text: '#333',
  },
  font: {
      family: 'Roboto, sans-serif',
      size: '16px',
  },
};
// Tema adaptado conforme suas cores e fontes
export const theme: Theme = {
  colors: {
      blue: '#1677ff',
      gray: 'rgba(237, 237, 237, 0.733)',
      black: '#333',
      primary: '#1677ff',
      secondary: '#399E5A',
      thirdary: '#555B6E',
      warning: '#F18805',
      danger: '#F05365',
      shadow_gray: 'rgba(237, 237, 237, 0.733)',
      shadow_blue: '#e6f4ff',
      highlights: '#1677ff',
      background: '#050708',
      text: '#333',
  },
  font: {
      family: 'Roboto, sans-serif',
      size: '16px',
  },
};

export default theme;