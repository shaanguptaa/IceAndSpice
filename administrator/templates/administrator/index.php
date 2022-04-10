<?php
  session_start();
  error_reporting(0);
  
  if ($_SESSION['login']=="0" || $_SESSION['login']=="") {
    $_SESSION['login']="0";
    header("Refresh:0; url=login/");
  }
  elseif ($_SESSION['login']=="1") {
    $_SESSION['login']="1";
  }
 
  require 'connect.php';
?>

<!DOCTYPE html>

<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta http-equiv="x-ua-compatible" content="ie=edge" />
  <title>Admin &ndash; Restaurant</title>
  <link rel="stylesheet" href="../assets/css/bootstrap/bootstrap.css">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css" />
  <!-- Google Fonts Roboto -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" />

    <link rel="stylesheet" href="assets/fonts/ionicons/css/ionicons.min.css">
    <link rel="stylesheet" href="assets/css/magnific-popup.css">

    <link rel="stylesheet" href="assets/fonts/fontawesome/css/font-awesome.min.css">
    
    
    <link rel="stylesheet" href="assets/css/slick.css">

    <link rel="stylesheet" href="assets/css/helpers.css">
  <!-- MDB -->
  <link rel="stylesheet" href="css/mdb.min.css" />
  <!-- Custom styles -->
  <link rel="stylesheet" href="css/admin.css" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js" integrity="sha512-d9xgZrVZpmmQlfonhQUvTR7lMPtO7NkZMkA0ABN3PHCbKA5nqylQ/yWlFAyY6hYgdF1Qh6nYiuADWwKB4C2WSw=="
    crossorigin="anonymous"></script>
    </script>

  <style type="text/css">
    body{
      overflow-x: hidden; 
    }
    .sidebar-right {
      position: fixed;
      float: right;
      top: 0;
      bottom: 0;
      right: 0;
      box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
      width: 30px;
      z-index: 700;
    }

    .list-group-item {
      padding-top: 15px !important;
      padding-bottom: 15px !important;
    }

    .welcome {
      font-size: 40px;
      font-family: sans-serif;
      padding-bottom: 10px;
      padding-left: 5px;
    }

   input[type=number] {
      -moz-appearance: textfield !important;
    }

    .add-item {
      color: black;
      float: right;
      margin-right: 20px;
      margin-top: -22px;
      padding-left: 10px;
      padding-right: 10px;

    }

    .add-item:hover, .add-item:active {
      background-color: rgba(0, 0, 0, 0.1);
    }

    .feedback-card:hover, .feedback-card:active {
      background-color: rgba(0, 0, 0, 0.1);
    }

    #load-more-feedbacks:hover, #load-more-feedbacks:active {
      color: blue;
    }

    #section-profile {
      display: none;
      position: fixed;
      padding: 0px;
      margin: 0px;
      z-index: 900;
      top: 0px;
      right: 0px;
      width: 80%;
      height: 100% ;
      background-color: #fbfbfb;
    }

    .icon-signout {
      position: relative;
      z-index: 100;
      top: -40px;
      padding-left: 20px;
    }

    .signout {
      padding-left: 50px;
      position: relative;
    }

    
  </style>
</head>

<body>
  <!--Main Navigation-->
  <header>
    <!-- Sidebar -->
    <nav id="sidebarMenu" class="collapse d-lg-block sidebar collapse bg-white">
      <div class="position-sticky">
        <div class="list-group list-group-flush mx-3 mt-4">
          <!-- Brand -->
          <a class="navbar-brand" href="index.php" style="justify-content: center;">
            <img src="../assets/images/restaurant/logo.png" height="30" alt="logo" loading="lazy" />
          </a>
          <hr>
          <a href="#" class="list-group-item list-group-item-action py-2 ripple" style="margin-top: -15px !important;" aria-current="true">
            <i class="fas fa-tachometer-alt fa-fw me-3"></i><span>Main dashboard</span></a>

          <a href="#section-reservations" class="list-group-item list-group-item-action py-2 ripple">
            <i class="fas fa-clock fa-fw me-3"></i><span>Reservations</span></a>

          <a href="#section-menu" class="list-group-item list-group-item-action py-2 ripple">
            <i class="fas fa-book-open fa-fw me-3"></i><span>Menu</span></a>

          <a href="#section-orders" class="list-group-item list-group-item-action py-2 ripple"><i
              class="fas fa-clipboard-list fa-fw me-3"></i><span>Orders</span></a>

          <a href="#section-feedback" class="list-group-item list-group-item-action py-2 ripple"><i
              class="fas fa-user-friends fa-fw me-3"></i><span>Customer Reviews</span></a>

          <a href="#" id="profile" class="list-group-item list-group-item-action py-2 ripple">
            <i class="fas fa-user-circle fa-fw me-3"></i><span>Profile</span></a>

          <form method="POST">
            <input href="#" type="submit" name="signout" value="Sign Out" class=" signout list-group-item list-group-item-action py-2 ripple">
            <i class="icon-signout fas fa-sign-out-alt fa-fw me-3"></i>
            
          </form>

          <?php 

            if (isset($_POST['signout'])) {
              session_destroy();
              header("Refresh:0; url=login/");
            }

          ?>

        </div>
      </div>
    </nav>
    <!-- Sidebar -->
          
        </div>
      </div>
    </nav>
    <!-- Sidebar -->
  </header>
  <!--Main Navigation-->

  <!--Main layout-->
  <main style="margin-right: -50px;">
    <div class="container pt-4">
      <h1 class="welcome">Welcome, <?php echo $_SESSION['name']; ?></h1>
      <!-- Section: Main chart -->
       <section class="mb-4 " id="section-reservations">
        <div class="card">
          <div class="card-header text-center py-3">
            <h5 class="mb-0 text-center">
              <strong>Recent Reservations</strong>
            </h5>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover text-nowrap" style="margin-top: -20px;">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email ID</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Date</th>
                    <th scope="col">Time</th>
                    <th scope="col">Persons</th>
                  </tr>
                </thead>
                <tbody>
                  <?php 
                      $tbl_name = 'bookings';
                      $sql = "SELECT * FROM `$tbl_name`";
                      $result = $mysqli -> query($sql);

                      if ($mysqli -> affected_rows <= 0) {
                        echo '<tr><td>No reservations till now</td></tr>';
                      } else {

                      while ($booking = $result -> fetch_assoc()) { ?>
                      <tr>
                        <td><?php echo $booking['name'] ?></td>
                        <td><?php echo $booking['email'] ?></td>
                        <td><?php echo $booking['phone'] ?></td>
                        <td><?php echo $booking['date'] ?></td>
                        <td><?php echo $booking['time'] ?></td>
                        <td><?php echo $booking['person'] ?></td>
                      </tr>
                <?php } }?>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>
      <!-- Section: Main chart -->

      <!--Section: Sales Performance KPIs-->
      <section class="mb-4 " id="section-menu" style="padding-top: 30px;">
        <div class="card">
          <div class="card-header text-center py-3">
            <h5 class="mb-0 text-center">
              <strong>Menu List</strong>
            </h5>
             <a class="add-item" id="add-item" href="#section-menu" onclick="addMenuItem()" data-toggle="modal" data-target="#add-menu-item">
               <i class="far fa-plus-square"> </i>  Add Item</a>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover text-nowrap" style="margin-top: -20px;">
                <thead>
                  <tr>
                    <th scope="col">Product ID</th>
                    <th scope="col">Product Name</th>
                    <th scope="col">Category</th>
                    <th scope="col">Status</th>
                    <th scope="col">Price</th>
                  </tr>
                </thead>
                <tbody>
                  <?php 
                      $tbl_name = 'menu';
                      $sql = "SELECT * FROM `$tbl_name`";
                      $result = $mysqli -> query($sql);

                      while ($food = $result -> fetch_assoc()) {
                    ?>
                      <tr onclick="editMenuItem(<?php echo $food['id']; ?>, '<?php echo $food['name']; ?>', '<?php echo $food['category']; ?>', '<?php echo $food['status']; ?>', <?php echo $food['price']; ?> )" data-toggle="modal" data-target="#edit-menu-item">
                        <td><?php echo $food['id'] ?></td>
                        <td><?php echo $food['name'] ?></td>
                        <td><?php echo $food['category'] ?></td>
                        <td><?php echo $food['status'] ?></td>

                        <td>&#x20B9; <?php echo $food['price'] ?> &sol;&ndash;</td>
                      </tr>
                <?php } ?>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>
      <!--Section: Sales Performance KPIs-->

    <div id="edit-menu-item" class="modal fade" role="popup">
      <div class="modal-dialog modal-dialog-centered modal-md">

        <!-- Modal content-->
        <div class="modal-content justify-content-center">
          <div class="modal-header">
            <h4 class="modal-title">Product Details:</h4>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>
          <div class="modal-body">
            <form method="POST">
              <div class="row">
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="pid">Product ID: </label>
                    <input type="text" name="pid" id="pid" class="form-control" readonly>
                  </div>
                </div>
                <div class="col-md-8">
                  <div class="form-group">
                    <label for="pname">Product Name: </label>
                    <input type="text" name="pname" id="pname" class="form-control" required>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="pcat">Category: </label>
                    <select name="pcat" id="pcat" class="form-control" required>
                      <option class="form-control" value="Main">Main</option>
                      <option class="form-control" value="Drink">Drink</option>
                      <option class="form-control" value="Dessert">Dessert</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="pstat">Status: </label>
                    <select name="pstat" id="pstat" class="form-control" required>
                      <option class="form-control" value="In Stock">In Stock</option>
                      <option class="form-control" value="Out of Stock">Out of Stock</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="p_price">Price: </label>
                    <input type="number" name="p_price" id="p_price" min="1" class="form-control" required>
                  </div>
                </div>
              </div>
              <div class="form-group" style="float: right; padding-top: 10px;">
                <input type="submit" name="delete" id="delete" value="Delete" onclick="return confirm('Are you sure?')" class="btn btn-danger" style=" margin-right: 20px;">
                <input type="submit" name="save" id="save" value="Save" class="btn btn-success" style=" margin-right: 20px;">
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>

      <div id="add-menu-item" class="modal fade" role="popup">
      <div class="modal-dialog modal-dialog-centered modal-md">

        <!-- Modal content-->
        <div class="modal-content justify-content-center">
          <div class="modal-header" style="padding-bottom: 0px;">
            <div>
              <h4 class="modal-title">Add Item:</h4>
              <p style="font-size: 15px;">Enter the details below to add a new item in the menu.</p>
            </div>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
          </div>
          <div class="modal-body">
            <form action="#section-menu" method="POST">
              <div class="row">
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="add_pid">Product ID: </label>
                    <input type="number" name="add_pid" id="add_pid" class="form-control" readonly>
                  </div>
                </div>
                <div class="col-md-8">
                  <div class="form-group">
                    <label for="pname">Product Name: </label>
                    <input type="text" name="pname" id="pname" class="form-control" required>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="pcat">Category: </label>
                    <select name="pcat" id="pcat" class="form-control" required>
                      <option class="form-control" value="Main">Main</option>
                      <option class="form-control" value="Drink">Drink</option>
                      <option class="form-control" value="Dessert">Dessert</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="pstat">Status: </label>
                    <select name="pstat" id="pstat" class="form-control" required>
                      <option class="form-control" value="In Stock">In Stock</option>
                      <option class="form-control" value="Out of Stock">Out of Stock</option>
                    </select>
                  </div>
                </div>
                <div class="col-md-4">
                  <div class="form-group">
                    <label for="p_price">Price: </label>
                    <input type="number" name="p_price" id="p_price" min="1" value="10" class="form-control" required>
                  </div>
                </div>
              </div>
              <div class="form-group" style="float: right; padding-top: 10px;">
                <input type="submit" name="delete" id="delete" value="Cancel" class="btn btn-danger" style=" margin-right: 20px;">
                <input type="submit" name="add" id="add" value="Add Item" class="btn btn-success" style=" margin-right: 20px;">
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>

    <?php 

      if (isset($_POST['add'])) {
        $id = $_POST['add_pid'];
        $name = $_POST['pname'];
        $category = $_POST['pcat'];
        $status = $_POST['pstat'];
        $price = $_POST['p_price'];

        $sql = "INSERT INTO `menu` VALUES ($id, '$name', '$category', '$status', $price)";
        if (!$mysqli -> query($sql)) {
          die("Cannot add item");
        } else {
          header("Refresh:0;");
        }
      }

      if (isset($_POST['save'])) {
        $id = $_POST['pid'];
        $name = $_POST['pname'];
        $category = $_POST['pcat'];
        $status = $_POST['pstat'];
        $price = $_POST['p_price'];
        
        $sql = "UPDATE `menu` SET `name`='$name',`category`='$category',`status`='$status',`price`=$price WHERE `id`=$id";
        if (!$mysqli -> query($sql)) {
          die("Cannot update data");
        } else { 
          header("Refresh:0;");
        }
      }
      elseif (isset($_POST['delete'])) {
        $id = $_POST['pid'];
        $sql = "DELETE FROM `menu` WHERE `id` = $id";
        if (!$mysqli -> query($sql)) {
          die("Couldn't delete product");
        } else {
          header("Refresh:0");
        }
      }

    ?>

      <script type="text/javascript">
        function editMenuItem(id, name, cat, status, price) {
          document.getElementById("pid").value = id;
          document.getElementById("pname").value = name;
          document.getElementById("pcat").value = cat;
          document.getElementById("pstat").value = status;
          document.getElementById("p_price").value = price;
        }
        function addMenuItem() {
          document.getElementById("add_pid").value = Math.floor(Math.random() * (9999 - 1000 + 1) ) + 1000;
        }
      </script>



      <!-- Section: Orders -->
      <section class="mb-4 " id="section-orders" style="padding-top: 30px;">
        <div class="card">
          <div class="card-header text-center py-3">
            <h5 class="mb-0 text-center">
              <strong>Recent Orders</strong>
            </h5>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover text-nowrap" style="margin-top: -20px;">
                <thead>
                  <tr>
                    <th scope="col">Order</th>
                    <th scope="col">Customer Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Location</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Amount</th>
                  </tr>
                </thead>
                <tbody>
                  <?php 
                      $tbl_name = 'orders';
                      $sql = "SELECT * FROM `$tbl_name`";
                      $result = $mysqli -> query($sql);

                      while ($order = $result -> fetch_assoc()) {
                    ?>
                      <tr>
                        <td><?php echo $order['item'] ?></td>
                        <td><?php echo $order['name'] ?></td>
                        <td><?php echo $order['email'] ?></td>
                        <td><?php echo $order['phone'] ?></td>
                        <td><?php echo $order['location'] ?></td>
                        <td><?php echo $order['quantity'] ?></td>
                        <td>&#x20B9; <?php echo $order['amount'] ?> &sol;&ndash;</td>
                      </tr>
                <?php } ?>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>


      <!-- Section: Feedbacks -->
      <section class="mb-4" id="section-feedback" style="padding-top: 30px;">
        <div class="card">
          <div class="card-header text-center py-3 "><h5 class="mb-0"><strong>Customer Feedbacks</strong></h5></div>
        </div>

        <?php 
          $tbl_name = 'feedbacks';
          $sql = "SELECT * FROM `$tbl_name` LIMIT 10";
          $result = $mysqli -> query($sql);
          if ($mysqli -> affected_rows <= 0) {
            echo '<div class="card py-3" style="padding-left: 10px;"> No feedbacks received till now</div>';
          } else {

          while ($feedback = $result -> fetch_assoc()) { ?>
            <div class="card feedback-card" style="border-bottom: 1px solid gray;">
              <div class="card-body" style="padding-left: 20px; padding-right: 20px;">
                <div class="row" style="padding-bottom: 10px;">
                  <span class="col-1" style="font-size: 15px; padding-left: 20px;"><i class="far fa-2x fa-user-circle"></i></span>
                  <h5 class="col-8" style="padding-top: 5px;"><?php echo $feedback['name']; ?></h5>
                <span class="col-3" style="padding-top: 5px;"><i class="far fa-calendar-alt"></i>&nbsp; <?php $date = new DateTime($feedback['time']); echo $date->format('Y-m-d') ?></span>
                </div>
                <div class="row">
                  <p style="padding-left: 90px;"><?php echo $feedback['msg'] ?></p>
                </div>
              </div>
            </div>
   <?php  } } ?>

      </section>

      <section class="mb-4" id="section-profile" style="padding-top: 30px;">
        <div class="container-fluid py-3">
          <form action="" method="POST">
            <div class="row py-3">
              <div class="col-3">
                <label style="float: right; font-size: 20px;">Email ID : </label>
              </div>
              <div class="col-5">
                <input type="text" name="email" id="email" value="<?php echo $_SESSION['email'] ?>">
              </div>
            </div>
            <div class="row py-3">
              <div class="col-3">
                <label style="float: right; font-size: 20px;">Name : </label>
              </div>
              <div class="col-5">
                <input type="text" name="name" id="name" value="<?php echo $_SESSION['name'] ?>">
              </div>
            </div>
            <div class="row py-3">
              <div class="col-3">
                <label style="float: right; font-size: 20px;">Phone : </label>
              </div>
              <div class="col-5">
                <input type="number" name="phone" id="phone" value="<?php echo $_SESSION['phone'] ?>">
              </div>
            </div>
            <div class="row py-3" id="pass">
              <div class="form-group">
                <label for="pwd" style="font-size: 20px;">Enter Current Password to Update Changes : </label>
                <input type="password" name="pwd" id="pwd" value="" required>
              </div>
            </div>
            <div class="row py-3">
              <div class="col-8">
                <center>
                  <input type="submit" name="edit" id="edit"  class="btn btn-success" value="Save Changes">
                </center>
              </div>
            </div>
          </form>
        </div>
      </section>

      <?php
        if (isset($_POST['edit'])) {
          $email = $_POST['email'];
          $phone = $_POST['phone'];
          $name = $_POST['name'];
          $pass = $_POST['pwd'];

          $tbl_name = "admins";
          $sql = "UPDATE `$tbl_name` SET `email`='$email', `name`='$name', `phone`='$phone' WHERE `password`=\"$pass\"";
          $mysqli -> query($sql);
          
          if ($mysqli -> affected_rows > 0) {
            echo '<script>alert("Credentials Updated Successfully!");</script>';
            $_SESSION['email'] = $email;
            $_SESSION['name'] = $name;
            $_SESSION['phone'] = $phone;
          } else {
             echo '<script>alert("Could not change Credentials");</script>';
          }
          // header("Refresh:0;");  

        }
      ?>


  </main>
  <!--Main layout-->
   <script src="assets/js/jquery.min.js"></script>
    
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>

    <script src="assets/js/slick.min.js"></script>
    <script src="assets/js/jquery.mb.YTPlayer.min.js"></script>

    <script src="assets/js/jquery.waypoints.min.js"></script>
    <script src="assets/js/jquery.easing.1.3.js"></script>
    
    <script src="assets/js/jquery.magnific-popup.min.js"></script>
    <script src="assets/js/magnific-popup-options.js"></script>
  <!-- MDB -->
  <script type="text/javascript" src="js/mdb.min.js"></script>
  <!-- Custom scripts -->
  <script type="text/javascript" src="js/admin.js"></script>

  <script type="text/javascript">
    $(document).on("click",".list-group-item", function () {
      if($(this).attr('id') == "profile") {
        $("#section-profile").toggle();
      } else {
        $("#section-profile").hide();
      }

    });
  </script>

</body>

</html>