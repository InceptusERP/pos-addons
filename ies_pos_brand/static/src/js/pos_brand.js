odoo.define('ies_pos_brand.logo', function(require) {
	"use strict";
	var screens = require('point_of_sale.screens');
	var core = require('web.core');
	var QWeb = core.qweb;
	
	screens.ScreenWidget.include({
		show : function() {
			var self = this;
			$(".pos-logo").attr('src',
					"/ies_pos_brand/static/src/img/" + this.pos.pos_session.config_id[0] +"_pos_logo.png?"+ Date.now());
			this._super();
		}
	});
	
	screens.ReceiptScreenWidget.include({
		render_receipt: function() {
			var order = this.pos.get_order();
	        this.$('.pos-receipt-container').html(QWeb.render('PosTicket',{
	                widget:this,
	                order: order,
	                receipt: order.export_for_printing(),
	                orderlines: order.get_orderlines(),
	                paymentlines: order.get_paymentlines(),
	                pos_image: "/ies_pos_brand/static/src/img/" + this.pos.pos_session.config_id[0] +"_pos_logo_bw.png?"+ Date.now(),
            }));
			
		},
	});

});
