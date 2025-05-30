import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";
import pluginReact from "eslint-plugin-react";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,ts,mts,cts,jsx,tsx}"],
    plugins: { js },
    extends: ["js/recommended"],
    rules: {
      "prefer-const": "warn",
    },
    settings: {
      react: {
        version: "detect", // 자동으로 현재 설치된 React 버전을 감지해서 사용
      },
    },
  },
  {
    files: ["**/*.{js,mjs,cjs,ts,mts,cts,jsx,tsx}"],
    languageOptions: {
      globals: globals.browser,
    },
  },
  tseslint.configs.recommended,
  pluginReact.configs.flat.recommended,
  {
    rules: {
      "prefer-const": "warn",
      "react/react-in-jsx-scope": "off", 
      "@typescript-eslint/no-unused-vars": "warn"
    },
  },
]);
