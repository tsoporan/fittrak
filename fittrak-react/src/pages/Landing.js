import React from "react";

import MainLayout from "../layouts/Main";

import { AppHeader } from "../components/Header";
import { AppBottomNavigation } from "../components/Navigation";
import { ContentWrapper } from "../components/Content";

const Landing = () => {
  return (
    <MainLayout>
      <AppHeader pageTitle="FitTrak" />
      <ContentWrapper>Body</ContentWrapper>
      <AppBottomNavigation />
    </MainLayout>
  );
};

export default Landing;
