import React from "react";

import MainLayout from "../layouts/Main";

import AppHeader from "../components/Header";
import { AppBottomNavigation } from "../components/Navigation";
import { ContentWrapper } from "../components/Content";

const Landing = props => {
  const { viewer } = props;

  return (
    <MainLayout>
      <AppHeader pageTitle="FitTrak" viewer={viewer} />
      <ContentWrapper>
        <p>
          Welcome {viewer.username}({viewer.email})
        </p>
      </ContentWrapper>
      <AppBottomNavigation />
    </MainLayout>
  );
};

export default Landing;
