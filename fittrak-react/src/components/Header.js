import React from "react";

import { withStyles } from "@material-ui/core/styles";

import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";

import IconButton from "@material-ui/core/IconButton";
import AccountCircle from "@material-ui/icons/AccountCircle";
import MenuItem from "@material-ui/core/MenuItem";
import Menu from "@material-ui/core/Menu";

const styles = {
  grow: {
    flexGrow: 1
  }
};

class AppHeader extends React.Component {
  state = {
    anchorEl: null
  };

  handleMenu = evt => {
    this.setState({
      anchorEl: evt.currentTarget
    });
  };

  handleClose = () => {
    this.setState({ anchorEl: null });
  };

  render() {
    const { pageTitle, viewer, classes } = this.props;
    const { anchorEl } = this.state;
    const open = Boolean(anchorEl);

    return (
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography
            style={{ fontFamily: "Kaushan Script" }}
            variant="h5"
            color="inherit"
            className={classes.grow}
          >
            {pageTitle}
          </Typography>
          <IconButton
            aria-owns={open ? "menu-appbar" : undefined}
            aria-haspopup="true"
            onClick={this.handleMenu}
            color="inherit"
          >
            <AccountCircle />
          </IconButton>
          <Typography color="inherit">Hi, {viewer.username}</Typography>
          <Menu
            id="menu-appbar"
            anchorEl={anchorEl}
            open={open}
            onClose={this.handleClose}
          >
            <MenuItem onClick={this.handleClose}>Profile</MenuItem>
            <MenuItem onClick={this.handleClose}>My account</MenuItem>
          </Menu>
        </Toolbar>
      </AppBar>
    );
  }
}

export default withStyles(styles)(AppHeader);
