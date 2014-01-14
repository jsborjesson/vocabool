(function () {

'use strict';
window.VB = window.VB || {};
VB.Models = VB.Models || {};

VB.Models.Term = Backbone.Model.extend({

    validate: function (attrs, options) {
        var errors = [];
        if (_.isEmpty(attrs.text)) {
            errors.push('Text can not be empty!');
        }
        if (!(attrs.language in VB.languages)) {
            errors.push('Invalid language: ' + attrs.language);
        }
        return _.any(errors) ? errors : null;
    },

    define: function () {
        var self = this,
            params = { define: null };

        this.fetch({ data: params }).done(function () {
            self.trigger('change');
        });
        return this;
    },

    translate: function (language) {
        // TODO: if not in settings.languages
        var self = this,
            params = { translate_to: language };


        this.fetch({ data: params }).done(function () {
            self.trigger('change');
        });
        return this;
    },


    translateAndDefine: function (language) {

        var params = {define: '', translate_to: language},
            self = this;

        this.fetch({ data: params }).done(function () {
            // TODO: Complete events
            self.trigger('change');
        });
        return this;

    }
});

VB.Models.Vocabulary = Backbone.Model.extend({
    initialize: function () {
        // create empty term collection with reference to this vocabulary
        this.terms = new VB.Collections.Terms([], { vocabulary: this });
    },
    urlRoot: '/api/vocabulary/'
});


VB.Models.Status = Backbone.Model.extend({
    defaults: {
        user: null,
        vocabulary: null,
    }
});

}());
