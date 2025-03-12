import React from "react";
import { RouteConfig } from './Routes';

import Home from "../pages/Home/index";
import Help from "../pages/Help";
import Error from "../pages/Error/index";
import NotFound from "../pages/Error/NotFound";
import Dashboard from "../pages/Dashboard";
import Items from "../pages/Items";
import Login from "../pages/Login";
import SignUp from "../pages/Signup";
import Users from "../pages/Users";
import EmissionFactors from "../pages/Parameters/EmissionFactors";
import Company from "../pages/Settings/Company";
import CompanyChangeForm from "../pages/Settings/Company/Changeform";

// Suas rotas
export const routes: RouteConfig[] = [
  { path: "*", element: <NotFound /> },
  { path: "/", element: <Home />, errorElement: <Error />, private: true },
  { path: "/help", element: <Help />, errorElement: <Error />, private: true },
  { path: "/sign-in", element: <Login />, errorElement: <Error />, private: false },
  { path: "/sign-up", element: <SignUp />, errorElement: <Error />, private: false },
  { path: "/items", element: <Items />, errorElement: <Error />, private: true },
  { path: "/dashboard", element: <Dashboard />, errorElement: <Error />, private: true },

  // Setetings
  { path: "/settings/users", element: <Users />, errorElement: <Error />, private: true },
  { path: "/settings/company", element: <Company />, errorElement: <Error />, private: true },
  { path: "/settings/company/add", element: <CompanyChangeForm />, errorElement: <Error />, private: true },

  // Parameters
  { path: "/parameters/emission-factors", element: <EmissionFactors />, errorElement: <Error />, private: true },
];